from browser_use import Agent, ChatGoogle
from dotenv import load_dotenv
import asyncio

# 1. This line loads your GEMINI_API_KEY from the .env file
load_dotenv()
# 3. Define the Goal/Task (Complex Data Extraction)
task = """
Go to http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html.
I want to create a two-site comparison page for this book.
Please extract the following information and present it as a single JSON object:
1. The book title.
2. The 5-star rating (as a number, e.g., 2).
3. The price (excluding the currency symbol).
4. The product description text.
5. The stock availability (e.g., 'In stock (22 available)').
"""

# ... leave the rest of the code the same ...

async def main():
    # 2. Define the Brain (using the key loaded above)
    llm = ChatGoogle(model="gemini-2.5-flash")

    # 3. Define the Goal/Task
    task = "Go to https://news.ycombinator.com/ and find the title of the post at position number 5. Output only the title text."

    # 4. Create the Agent with the Goal and the Brain
    agent = Agent(task=task, llm=llm)

    # 5. Run the agent and wait for it to finish
    history = await agent.run()

    # 6. Print the final result (the answer it found)
    print("\n--- AGENT COMPLETE ---")
    print("Final Result:", history.final_result())

if __name__ == "__main__":
    asyncio.run(main())