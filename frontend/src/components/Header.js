import React, { useState, useContext, useEffect } from 'react';
import '../assets/scss/header.scss';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { AppContext } from '../context/AppContext';

const Header = () => {
  const { cart } = useContext(AppContext);

  return (
    <header>
      <div className="container">
        <div className="logo"><a href="/">LOGO</a></div>
        <div className="tool_nav">
          <div className="cart">
            <a href="/cart">
              <FontAwesomeIcon icon="shopping-cart" />
              <span>{cart.length}</span>
            </a>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;