
import React, { useState, useEffect } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { IoMdArrowRoundBack } from 'react-icons/io';

const NewsDetails = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [news, setNews] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const sendBackToHome = () => {
    navigate('/');
  };

  useEffect(() => {
    const fetchNewsItem = async () => {
      try {
        const response = await fetch(`${process.env.REACT_APP_BACKEND_URL}/api/get-news/${id}`);
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await response.json();
        setNews(data);
      } catch (error) {
        setError(error.message || 'Something went wrong');
      } finally {
        setLoading(false);
      }
    };

    fetchNewsItem();
  }, [id]);

  if (loading) {
    return <div className="container mx-auto p-4">Loading...</div>;
  }

  if (error) {
    return <div className="container mx-auto p-4">Error: {error}</div>;
  }

  if (!news) {
    return <div className="container mx-auto p-4">News not found.</div>;
  }

  const timeString = new Date(news.time * 1000).toLocaleString();

  return (
    <div className="container mx-auto p-4 bg-secondary">
      <button
        className="p-2 bg-secondary text-secondary hover:border-2 hover:border-[#E97018] hover:border-solid flex flex-row items-center my-8 rounded-lg"
        onClick={sendBackToHome}
      >
        <IoMdArrowRoundBack /> Home
      </button>
      <a
        className="text-3xl font-bold mb-4 no-underline text-secondary"
        href={news.url}
        target="_blank"
        rel="noopener noreferrer"
      >
        {news.title}
      </a>
      <p className="text-gray-600 mb-2">
        By {news.by} | Score: {news.score} | Posted on {timeString}
      </p>
      <a
        href={news.url}
        target="_blank"
        rel="noopener noreferrer"
        className="text-blue-600 hover:underline w-full flex justify-start"
      >
        Read the full story
      </a>
    </div>
  );
};

export default NewsDetails;
