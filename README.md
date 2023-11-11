<div align="center">
    <img src="https://pbs.twimg.com/profile_images/1653232294151475200/FyoHlx_s_400x400.jpg" alt="Lenster Logo" height="100" width="100">
    <h1>CharityGPT</h1>
    <strong>An AI model specifically designed for parsing news headlines to classify whether a DAO should raise funds or not. </strong>
</div>
<br>
<div align="center">
    <div>
    <a href="https://lenster.xyz/u/yoginth">
        <img src="https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white" alt="Lens">
    </a>
    <a href="https://vercel.com/lenster?utm_source=Lenster&utm_campaign=oss">
        <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Vercel">
    </a>
    <a href="https://vercel.com/lenster?utm_source=Lenster&utm_campaign=oss">
        <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue">
    </a>
    </div>
</div>
<br />

## CharityGPT
CharityGPT, an AI model specifically designed for parsing news headlines to classify whether a DAO should raise funds or not. 

## Overview
This Flask application provides an API service for fetching news relevant to specific charity categories. It interfaces with a news API and an LLM (Language Learning Model) to filter headlines suitable for raising funds for charities.

## Installation

### Prerequisites
- Python 3.x
- pip (Python package manager)

### Setup
1. **Clone the Repository**
```
git clone https://github.com/shivam017arora/chainlink-ai-news-fund-raiser.git
cd chainlink-ai-news-fund-raiser
```


2. **Install the requirements**

```sh
pip install -r requirements.txt
```

3. **Set up environment variables**

Copy the `.env.example` file to create a `.env` that will store your environment variables.

```sh
cp .env.example .env
```

Edit the `.env` file with your specific configurations.

4. **Run the Flask application**

```sh
python serv.py
```

By default, the application will run on `http://localhost:8912`.

## Testing

To run the tests, use the following command:

```
pytest
```

## API Documentation

### Demo 
<img width="710" alt="Screenshot 2023-11-11 at 11 47 06 AM" src="https://github.com/shivam017arora/chainlink-ai-news-fund-raiser/assets/26146104/b85acbe1-a5fd-4282-9eb3-31277b31bf8f">

### Endpoint: `/api/charity`

#### Method: `POST`

#### Description:
This endpoint accepts POST requests with a JSON payload containing a 'category' field. It fetches news related to the specified charity category and returns headlines suitable for raising funds for charities.

#### Request Format:
```json
{
    "category": "string"
}
```

#### Response Format:
```json
{
    "result": "array or string (depending on LLM response)"
}
```

#### Status Codes:
- `201 Created`: The request was successful, and relevant news headlines are returned.
- `400 Bad Request`: The request is invalid (e.g., missing required fields).

#### Example Usage:

**Request:**
```bash
curl -X POST http://localhost:8912/api/charity \
     -H "Content-Type: application/json" \
     -d '{"category": "health"}'
```

**Response:**
```json
{
    "result": ["Headline 1 relevant to health category", "Headline 2 relevant to health category"]
}
```

# Future Scope

1. Enhanced Source Selection
Future versions of this application could include the ability to customize news sources. Users could specify preferred news sources or exclude certain sources, offering more tailored news aggregation.

2. Broader Language Support
Expanding the application to support multiple languages can make the service accessible to a more diverse user base and global charity organizations.

3. Advanced Filtering Options
Implementing advanced filtering based on keywords, date ranges, or specific geographic locations can refine the news results, making the service more relevant and effective for users.

4. Integration with Social Media Platforms
Allowing the app to fetch and analyze news from social media platforms could provide more real-time and grassroots-level insights, which are crucial for some charity campaigns.

5. User Interface for Non-Technical Users
Developing a user-friendly web interface can make the application more accessible to non-technical users, allowing charities to leverage this tool without needing programming knowledge.

## 💕 Contributors

We love contributors! Feel free to contribute to this project but please read the [Contributing Guidelines](CONTRIBUTING.md) before opening an issue or PR so you understand the branching strategy and local development environment.

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Shivam Arora - [@Shivam017arora](https://twitter.com/Shivam017arora)

<p align="right">(<a href="#top">back to top</a>)</p>

## License

CharityGPT is open-sourced software licensed under the © [MIT](LICENSE).
