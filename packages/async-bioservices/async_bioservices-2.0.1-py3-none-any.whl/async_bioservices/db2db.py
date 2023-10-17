import asyncio
import pandas as pd
from bioservices import BioDBNet
from multiprocessing import Value
from typing import Union, List, Iterable

from async_bioservices.input_database import InputDatabase
from async_bioservices.output_database import OutputDatabase
from async_bioservices.taxon_id import TaxonID


class _AsyncBioservices:
    biodbnet: BioDBNet = None
    
    def __init__(self, quiet: bool, cache: bool):
        if _AsyncBioservices.biodbnet is None:
            biodbnet = BioDBNet(verbose=not quiet, cache=cache)  # Invert quiet to verbose
            biodbnet.services.settings.TIMEOUT = 60
            _AsyncBioservices.biodbnet = biodbnet
            self.biodbnet = _AsyncBioservices.biodbnet
        else:
            self.biodbnet = _AsyncBioservices.biodbnet


async def _execute_db2db(
    biodbnet: BioDBNet,
    input_values: List[str],
    input_db: str,
    output_db: List[str],
    taxon_id: int,
    delay: int = 10
) -> pd.DataFrame:
    conversion = await asyncio.to_thread(
        biodbnet.db2db,
        input_db=input_db,
        output_db=output_db,
        input_values=input_values,
        taxon=taxon_id
    )
    
    # If the above db2db conversion didn't work, try again until it does
    if not isinstance(conversion, pd.DataFrame):
        # Errors will occur on a timeouut. If this happens, split our working dataset in two and try again
        first_set: List[str] = input_values[:len(input_values) // 2]
        second_set: List[str] = input_values[len(input_values) // 2:]
        
        await asyncio.sleep(delay)
        first_conversion: pd.DataFrame = await _execute_db2db(
            biodbnet=biodbnet, input_values=first_set, input_db=input_db,
            output_db=output_db, taxon_id=taxon_id, delay=delay
        )
        second_conversion: pd.DataFrame = await _execute_db2db(
            biodbnet=biodbnet, input_values=second_set, input_db=input_db,
            output_db=output_db, taxon_id=taxon_id, delay=delay
        )
        
        return pd.concat([first_conversion, second_conversion])
    
    return conversion


async def _worker(
    queue: asyncio.Queue,
    result_queue: asyncio.Queue,
    num_items: int,
    num_collected: Value,
    quiet: bool
):
    if not quiet:
        print("\rCollecting genes...", end="")
    
    while not queue.empty():
        item = await queue.get()
        db2db_result = await item
        await result_queue.put(db2db_result)
        
        num_collected.value += len(db2db_result)
        if not quiet:
            print(f"\rCollecting genes... {num_collected.value} of {num_items} finished", end="")
        
        queue.task_done()


async def db2db(
    input_values: Union[List[str], List[int]],
    input_db: InputDatabase,
    output_db: Union[OutputDatabase, Iterable[OutputDatabase]] = (
        OutputDatabase.GENE_SYMBOL.value,
        OutputDatabase.GENE_ID.value,
        OutputDatabase.CHROMOSOMAL_LOCATION.value
    ),
    taxon_id: Union[TaxonID, int] = TaxonID.HOMO_SAPIENS,
    quiet: bool = False,
    remove_duplicates: bool = False,
    cache: bool = True,
    delay: int = 5,
    concurrency: int = 8,
    batch_length: int = 300
) -> pd.DataFrame:
    pass
    """
    Convert gene information using BioDBNet

    :param input_values: A list of genes in "input_db" format
    :param input_db: The input database to use (default: "Ensembl Gene ID")
    :param output_db: The output format to use (default: ["Gene Symbol", "Gene ID", "Chromosomal Location"])
    :param delay: The delay in seconds to wait before trying again if bioDBnet is busy (default: 15)
    :param cache: Should results be cached
    :param taxon_id: The taxon ID to use (default: 9606)
    :param quiet: Should the conversions show output or not?
    :param remove_duplicates: Should duplicate values be removed from the resulting dataframe?
    :param concurrency: The number of concurrent connections to make to BioDBNet
    :param batch_length: The maximum number of items to convert at a time
    :return: A dataframe with specified columns as "output_db" (Default is HUGO symbol, Entrez ID, and chromosome start and end positions)
    """
    input_values: List[str] = [str(i) for i in input_values]
    input_db_value: str = input_db.value
    
    output_db_values: List[str]
    if isinstance(output_db, OutputDatabase):
        output_db_values = [output_db.value]
    else:
        output_db_values = [str(i.value) for i in output_db]
    
    # Check if input_db_value is in output_db_values
    if input_db_value in output_db_values:
        raise ValueError("Input database cannot be in output database")
    
    if isinstance(taxon_id, TaxonID):
        taxon_id_value: int = int(taxon_id.value)
    else:
        taxon_id_value: int = int(taxon_id)
    
    # Validate input settings
    if concurrency > 20:
        raise ValueError(f"Concurrency cannot be greater than 20. {concurrency} was given.")
    
    if batch_length > 500 and taxon_id_value == TaxonID.HOMO_SAPIENS.value:
        raise ValueError(f"Batch length cannot be greater than 500 for Homo Sapiens. {batch_length} was given.")
    elif batch_length > 300 and taxon_id_value == TaxonID.MUS_MUSCULUS.value:
        raise ValueError(f"Batch length cannot be greater than 300 for Mus Musculus. {batch_length} was given.")
    
    biodbnet = _AsyncBioservices(quiet=quiet, cache=cache)
    biodbnet.biodbnet.services.TIMEOUT = 60
    
    # Define variables
    # Create queues to hold results
    queue: asyncio.Queue = asyncio.Queue()
    result_queue: asyncio.Queue = asyncio.Queue()
    # Hold number of items complete
    num_collected: Value = Value('i', 0)
    
    # Create tasks to be completed
    for i in range(0, len(input_values), batch_length):
        # Define an upper range of values to take from input_values
        upper_range = min(i + batch_length, len(input_values))
        task = _execute_db2db(
            biodbnet=biodbnet.biodbnet,
            input_values=input_values[i:upper_range],
            input_db=input_db_value,
            output_db=output_db_values,
            taxon_id=taxon_id_value,
            delay=delay
        )
        queue.put_nowait(task)
    
    workers = [
        asyncio.create_task(_worker(
            queue=queue,
            result_queue=result_queue,
            num_items=len(input_values),
            num_collected=num_collected,
            quiet=quiet,
        ))
        for _ in range(concurrency)
    ]
    
    await asyncio.gather(*workers)
    await queue.join()
    for w in workers:
        w.cancel()
    
    conversion_results = []
    while not result_queue.empty():
        conversion_results.append(await result_queue.get())
    
    if not quiet:
        print("")
    main_df: pd.DataFrame = pd.DataFrame()
    item: pd.DataFrame
    for i, item in enumerate(conversion_results):
        item.reset_index(inplace=True)
        main_df = pd.concat([main_df, item])
        if not quiet:
            print(f"Concatenating dataframes... {i + 1} of {len(conversion_results)}" + " " * 50, end="\r")
    
    if not quiet:
        print("")
    
    # Remove duplicate index values
    if remove_duplicates:
        main_df = main_df[~main_df.index.duplicated(keep='first')]
    
    # Move index to column
    main_df.reset_index(inplace=True, drop=True)
    return main_df


if __name__ == "__main__":
    asyncio.run(db2db(
        input_values=[str(i) for i in range(1, 10_000)],
        input_db=InputDatabase.GENE_ID,
        output_db=OutputDatabase.GENE_SYMBOL,
    ))
