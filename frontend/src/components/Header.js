import React from 'react';
import '../assets/scss/header.scss';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

const Header = () => {
  return (
    <header>
      <div className="container">
        <div className="logo"><a href="/">LOGO</a></div>
        <div className="tool_nav">
          <div className="cart">
            <a href="/cart">
              <FontAwesomeIcon icon="shopping-cart" />
              <span>0</span>
            </a>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;