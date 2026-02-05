import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.google import Gemini # Or use Gemini/Anthropic
from tools import search_tmdb_movies # This is the tool we made in Step 3

# Define the Agent
movie_agent = Agent(
    name="Marquee",
    model=Gemini(id="gemini-2.5-flash"), 
    tools=[search_tmdb_movies], # Tell the agent it is allowed to use this
    instructions=[
        "You are 'Marquee', a sophisticated cinema research agent.",
        "When a user asks for a movie, use the search_tmdb_movies tool to get real data.",
        "Always provide the release year and a brief 'why you'd like it' summary.",
        "If you can't find something, suggest a classic in the same genre.",
    ],
    debug_mode=True,
    markdown=True,
)

def main():
    print("🎬 Marquee CLI: Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        
        # This keeps the agent "alive" and talking to you
        movie_agent.print_response(user_input)

if __name__ == "__main__":
    main()

# Start the conversation
movie_agent.print_response("Find me some movies similar to Interstellar")
