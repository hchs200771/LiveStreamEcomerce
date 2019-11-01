import React from 'react';
import '../assets/scss/cart.scss'

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

const cartsData = [
  {
    id: 1,
    name: "LOL英雄聯盟公仔模型模型 放逐之刃 瑞雯 永久英雄",
    image: "http://i03.c.aliimg.com/img/ibank/2014/229/806/1452608922_2062856041.jpg",
    original_price: 1499,
    special_price: 999,
  },
  {
    id: 2,
    name: "英雄聯盟LOL 吉茵珂絲公仔 暴走蘿莉大炮戰鬥版大號模型",
    image: "http://gw3.alicdn.com/bao/uploaded/i3/TB1vBQYKpXXXXX.XVXXXXXXXXXX_!!0-item_pic.jpg",
    original_price: 1499,
    special_price: 999,
  },
  {
    id: 3,
    name: "正義聯盟公仔模型模型 蝙蝠俠",
    image: "http://big-er.com/big_pic/2015/1876/Dawn_Of_Justice_Play-Arts_Kai_Batman_01__scaled_600.jpg",
    original_price: 1499,
    special_price: 999,
  },
  {
    id: 4,
    name: "正義聯盟公仔模型模型 神力女超人",
    image: "https://img.ruten.com.tw/s2/9/1b/ba/21618640863162_716.jpg",
    original_price: 1499,
    special_price: 999,
  },
];
const cartRows = cartsData.map(cartRow => {
  return (
    <div className="content">
      <div className="items">
        <div className="product_image">
          <a href={"/products/" + cartRow.id}>
            <img src={cartRow.image} />
          </a>
        </div>
        <h2><a href={"/products/" + cartRow.id}>{cartRow.name}</a></h2>
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
      <div className="price">${cartRow.original_price}</div>
      <div className="total">${cartRow.special_price}</div>
    </div>
  );
});

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
              {cartRows}
            </div>
          </div>
          <div className="row">
            <div className="col-md-8 col-sm-12">
              <div className="buyers_form">
                <h3>收件者資料：</h3>
                <div className="name">
                  <label>姓名：</label>
                  <input type="text" />
                </div>
                <div className="phone">
                  <label>電話：</label>
                  <input type="text" />
                </div>
                <div className="email">
                  <label>E-mail：</label>
                  <input type="email" />
                </div>
                <div className="address">
                  <label>地址：</label>
                  <input type="text" />
                </div>
                <div className="pay">
                  <div>
                    <label>信用卡：</label>
                    <input type="radio" />
                  </div>
                  <div>
                    <label>ATM：</label>
                    <input type="radio" />
                  </div>
                  <div>
                    <label>貨到付款：</label>
                    <input type="radio" />
                  </div>
                </div>
                <button className="checkout">
                  <FontAwesomeIcon icon="arrow-right" />
                  馬上結帳
                </button>
              </div>
            </div>
            <div className="col-md-4 col-sm-12">
              <div className="subtotals">
                <div className="upper_block">
                  <div className="subtotal">
                    <b>小計：</b>$6993
                  </div>
                  <div className="subtotal">
                    <b>小計：</b>$0
                  </div>
                  <div className="subtotal">
                    <b>折扣：</b>
                  </div>
                </div>
                <div className="lower_block">
                  <div className="the_total">
                    <b>合計：</b>$6993
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default MyCart;