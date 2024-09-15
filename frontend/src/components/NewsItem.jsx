import React from 'react';
import { Link } from 'react-router-dom';

const NewsItem = ({ news }) => {
  const timeString = new Date(news.time * 1000).toLocaleString();

  return (
    <div className="p-4 border-b bg-secondary">
      <a
        href={news.url}
        target="_blank"
        rel="noopener noreferrer"
        className="text-xl font-semibold text-secondary"
      >
        {news.title}
      </a>
      <p className="text-gray-600">
        By {news.author} | Score: {news.score} | Posted on {timeString}
      </p>
      <Link to={`/news/${news.id}`} className="text-blue-600 hover:underline">
        Read more
      </Link>
    </div>
  );
};

export default NewsItem;
