import React, { useState, useEffect } from 'react';
import NewsItem from '../components/NewsItem';
// import { newsData } from '../dummy.data';

const NewsPage = () => {
  const [newsData, setNewsData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(
          `${process.env.REACT_APP_BACKEND_URL}/api/get-news`
        );
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await response.json();
        setNewsData(data);
      } catch (error) {
        setError(error.message || 'Something went wrong');
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) {
    return (
      <div className="container mx-auto p-4 flex flex-col justify-center items-center">
        <svg width="100" height="100" viewBox="0 0 100 100">
          <circle
            cx="50"
            cy="50"
            r="20"
            stroke="#333"
            stroke-width="4"
            fill="none"
          />
          <circle
            cx="50"
            cy="50"
            r="20"
            stroke="#e97018 "
            stroke-width="4"
            fill="none"
            stroke-linecap="round"
          >
            <animateTransform
              attributeName="transform"
              type="rotate"
              from="0 50 50"
              to="360 50 50"
              dur="1s"
              repeatCount="indefinite"
            />
          </circle>
        </svg>

        <span>Loading...</span>
      </div>
    );
  }
  if (newsData.length === 0) {
    return <div className="container mx-auto p-4">No news available.</div>;
  }
  if (error) {
    return <div className="container mx-auto p-4">Error: {error}</div>;
  }
  return (
    <div className="container mx-auto p-4 bg-secondary">
      {newsData.map((news) => (
        <NewsItem key={news.id} news={news} />
      ))}
    </div>
  );
};

export default NewsPage;
