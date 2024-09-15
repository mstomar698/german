import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import NewsPage from './NewsPage';

beforeEach(() => {
  fetch.resetMocks();
});

test('renders loading state initially', () => {
  render(<NewsPage />);
  expect(screen.getByText(/loading/i)).toBeInTheDocument();
});

process.env.REACT_APP_BACKEND_URL = 'http://localhost:8000';

beforeEach(() => {
  fetch.resetMocks();
});

test('renders news items after fetching', async () => {
  const mockNewsData = [
    {
      id: 1,
      title: 'Test News 1',
      by: 'Author 1',
      time: 1633036800,
      url: 'https://example.com/1',
      score: 100,
    },
    {
      id: 2,
      title: 'Test News 2',
      by: 'Author 2',
      time: 1633123200,
      url: 'https://example.com/2',
      score: 200,
    },
  ];

  fetch.mockResponseOnce(JSON.stringify(mockNewsData));

  render(<NewsPage />);

  expect(fetch).toHaveBeenCalledWith('http://localhost:8000/api/get-news');
});

test('renders error state on API failure', async () => {
  fetch.mockRejectOnce(new Error('Network Error'));

  render(<NewsPage />);

  await waitFor(() => {
    expect(screen.getByText(/No news available./i)).toBeInTheDocument();
  });
});

test('renders no news available when data is empty', async () => {
  fetch.mockResponseOnce(JSON.stringify([]));

  render(<NewsPage />);

  await waitFor(() => {
    expect(screen.getByText(/No news available/i)).toBeInTheDocument();
  });
});
