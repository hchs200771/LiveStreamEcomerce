import React from 'react';
import '../assets/scss/header.scss';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

const Header = () => {
  return (
    <header>
      <div className="container">
        <div className="logo">LOGO</div>
        <div className="tool_nav">
          <div className="cart">
            <a href="#">
              <FontAwesomeIcon icon="shopping-cart" />
            </a>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;