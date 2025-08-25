import { render, screen } from '@testing-library/react';
import App from '../App';

describe('App component', () => {
  test('renders S3 Challenge title', () => {
    render(<App />);
    expect(screen.getByText(/S3 Challenge/i)).toBeInTheDocument();
  });

  test('renders Challenge 1 button', () => {
    render(<App />);
    expect(screen.getByText(/Challenge 1/i)).toBeInTheDocument();
  });

  test('renders Challenge 2 button', () => {
    render(<App />);
    expect(screen.getByText(/Challenge 2/i)).toBeInTheDocument();
  });

  test('renders Challenge 3 button', () => {
    render(<App />);
    expect(screen.getByText(/Challenge 3/i)).toBeInTheDocument();
  });

  test('renders Challenge 4 button', () => {
    render(<App />);
    expect(screen.getByText(/Challenge 4/i)).toBeInTheDocument();
  });
});