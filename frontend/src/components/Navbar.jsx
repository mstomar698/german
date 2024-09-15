import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav className="bg-primary p-4 flex justify-center items-center text-center">
      <Link to="/" className="text-primary text-lg font-bold">
      Top 10 News
      Stories <br />
      <span className='font-extrabold'>Hacker News</span>
      </Link>
    </nav>
  );
};

export default Navbar;
