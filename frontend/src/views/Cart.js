import React from 'react';
import '../assets/scss/cart.scss'

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

const MyCart = () => {
  return(
    <div id="cart">
      <div className="cart_head">
        <div className="container">
          <div className="row">
            <h2>
              我的購物車
              <FontAwesomeIcon icon="chevron-right" />
            </h2>
            <button className="checkout">結帳</button>
          </div>
        </div>
      </div>
      <div className="cart_body">
        <div className="container">
          <div className="row">
            <div className="col-sm-12">
              <div className="table">
                <div className="table_head">
                  <div className="content">
                    <div className="items">項目</div>
                    <div className="quantity">數量</div>
                    <div className="price">價格</div>
                    <div className="total">總共</div>
                  </div>
                </div>
                <div className="table_body">
                  <div className="content">
                    <div className="items">
                      <div className="product_image">
                        <a href="">
                          <img src="http://big-er.com/big_pic/2015/1876/Dawn_Of_Justice_Play-Arts_Kai_Batman_01__scaled_600.jpg" />
                        </a>
                      </div>
                      <h2><a href="">《蝙蝠俠對超人：正義曙光》 Play Arts 改 蝙蝠俠</a></h2>
                    </div>
                    <div className="quantity">
                      <div className="block">
                        <div className="control">
                          <button className="dec disabled">−</button>
                          <input type="text" value="1" />
                          <button className="inc">＋</button>
                        </div>
                        <button className="remove">移除項目</button>
                      </div>
                    </div>
                    <div className="price">$999</div>
                    <div className="total">$999</div>
                  </div>
                </div>
              </div>
            </div>
            <div className="col-lg-3 col-sm-12">
              123
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default MyCart;