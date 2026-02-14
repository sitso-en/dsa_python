"""Question 10 (Bonus: Async + HTTP Request) 
Write an async function fetch_posts() that fetches posts from 
https://jsonplaceholder.typicode.com/posts using aiohttp or httpx and prints 
the titles of the first 5 posts."""

import asyncio
import aiohttp

async def pull_user_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    async with aiohttp.ClientSession() as request:
        async with request.get(url) as result: 
            data = await result.json() for
            
            for i in range(5):# just print first 5 titles
                print(data[i]["title"])

#run the function
asyncio.run(pull_user_posts())
