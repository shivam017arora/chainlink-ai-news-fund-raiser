from newsapi import NewsApiClient
from chain import filter, classify
from dotenv import dotenv_values, load_dotenv
import json
import os

config = {
    **dotenv_values(".env"),  # load shared development variables
    **dotenv_values(".env.secret"),  # load sensitive variables
    **os.environ,  # override loaded values with environment variables
}

def fetch_news(api_key, query, sources=None, domains=None, from_date=None, to_date=None, language='en', sort_by='publishedAt', page=1):
    # Initialize the News API client
    newsapi = NewsApiClient(api_key=api_key)

    # Fetch news articles
    all_articles = newsapi.get_everything(q=query,
                                          sources=sources,
                                          domains=domains,
                                          from_param=from_date,
                                          to=to_date,
                                          language=language,
                                          sort_by=sort_by,
                                          page=page)

    return all_articles

def main(category):
    api_key = config['NEWS_API_KEY']  # Replace with your News API key

    # Example query for a charity focused on blind children
    query = category

    # Fetch news
    articles = fetch_news(api_key, query)
    headlines = [article['title'] for article in articles['articles']]
    headlines_prompt = ""
    for index, headline in enumerate(headlines):
        headlines_prompt += f"Headline {index}: {headline}\n"""
    
    # Get the headlines that are most relevant to the charity
    filtered_headlines = filter(headlines_prompt)
    filtered_headlines = json.loads(filtered_headlines)['relevant']

    print("The most relevant headlines are: ")
    relevant_headlines = [headlines[index] for index in filtered_headlines]
    for headline in relevant_headlines:
        print(headline)
    
    should_raise_funds_prompt = ""
    for index, headline in enumerate(relevant_headlines):
        should_raise_funds_prompt += f"Headline {headline}\n Desc: {articles['articles'][index]['description']}\n"""
    
    llm_response = classify(should_raise_funds_prompt)
    llm_response = json.loads(llm_response)['result']
    return llm_response


# Initialize Flask app
from flask import Flask, jsonify, request, abort
app = Flask(__name__)

@app.route('/api/charity', methods=['POST'])
def charity():
    if not request.json or not 'category' in request.json:
        abort(400)
    category = request.json['category']
    llm_response = main(category)
    return jsonify({'result': llm_response}), 201


if __name__ == "__main__":
    app.run(debug=True, port=8912)
