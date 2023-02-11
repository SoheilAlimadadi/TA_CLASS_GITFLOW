import asyncio
from datetime import datetime
# def gen():
#     yield 3
#     return 4

# try:
#     a = gen()
#     next(a)
#     next(a)
#     next(a)
# except StopIteration as e:
#     print(e)


async def calculation():
    return sum([x ** 2 for x in range(10_000_000)])

async def main():
    task_one = asyncio.create_task(calculation())
    task_two = asyncio.create_task(calculation())

    await task_one
    print(datetime.now())
    await task_two
    print(datetime.now())

print(datetime.now())
asyncio.run(main())
