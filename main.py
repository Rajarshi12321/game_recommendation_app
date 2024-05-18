from game_recommendation_app.components.data_querying import my_query
import os

os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

ans = my_query("can you reccomend me some fantasy games? about 2 games")

print(ans)
