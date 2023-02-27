import asyncio

class BatchFetcher:
    # The `database` has an `async_fetch` method
    # that you should use in your code. This method
    # takes in a record id and returns a record.
    def __init__(self, database):
        self.data = database

    async def fetch_records(self, ids_list):
        tasks = []
        results = []
        for each in ids_list:
            task = asyncio.create_task(self.data.async_fetch(each))
            tasks.append(task)
        
        for each in tasks:
            result = await each
            results.append(result)
        return results
    # Write your code here.