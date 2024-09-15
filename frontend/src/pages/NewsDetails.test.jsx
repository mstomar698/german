import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import NewsDetails from './NewsDetails';
import { BrowserRouter } from 'react-router-dom';
import { useParams } from 'react-router';

jest.mock('react-router', () => ({
  ...jest.requireActual('react-router'),
  useParams: jest.fn(),
}));

beforeEach(() => {
  fetch.resetMocks();
});

test('renders loading state initially', () => {
  useParams.mockReturnValue({ id: '1' });
  render(
    <BrowserRouter>
      <NewsDetails />
    </BrowserRouter>
  );
  expect(screen.getByText(/loading/i)).toBeInTheDocument();
});

test('renders news details after fetching', async () => {
  useParams.mockReturnValue({ id: '1' });

  const mockNewsItem = {
    id: 1,
    title: 'Test News 1',
    by: 'Author 1',
    time: 1633036800,
    url: 'https://example.com/1',
    score: 100,
  };

  fetch.mockResponseOnce(JSON.stringify(mockNewsItem));

  render(
    <BrowserRouter>
      <NewsDetails />
    </BrowserRouter>
  );

  await waitFor(() => {
    expect(screen.getByText('Test News 1')).toBeInTheDocument();
  });
});

test('renders error state on API failure', async () => {
  useParams.mockReturnValue({ id: '1' });

  fetch.mockRejectOnce(new Error('Network Error'));

  render(
    <BrowserRouter>
      <NewsDetails />
    </BrowserRouter>
  );

  await waitFor(() => {
    expect(screen.getByText(/Error: Network Error/i)).toBeInTheDocument();
  });
});

test('renders news not found when data is null', async () => {
  useParams.mockReturnValue({ id: '1' });

  fetch.mockResponseOnce(JSON.stringify(null));

  render(
    <BrowserRouter>
      <NewsDetails />
    </BrowserRouter>
  );

  await waitFor(() => {
    expect(screen.getByText(/News not found/i)).toBeInTheDocument();
  });
});
