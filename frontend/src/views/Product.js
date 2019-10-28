import React from 'react';
import '../assets/scss/product.scss'

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

const Product = () => {
  return (
    <div id="product">
      <div className="container">
        <div className="row">
          <div className="product_image col-md-6">
            <img src="https://cf.shopee.tw/file/ad118a574093b7d6ccbe469bfd0ec3a1" />
          </div>
          <div class="product_info col-md-6">
            <div className="product_title">
              <h1>英雄聯盟 世界大賽官方正版公仔 脈衝火焰 伊澤瑞爾</h1>
            </div>
            <div className="product_brief">
              <p>超人氣角色 伊澤瑞爾公仔 數量有限要買要快喔~</p>
            </div>
            <div className="product_price row">
              <div className="onsale">
                <span>特價</span>
                <b>NT $999</b>
              </div>
              <div className="ori_price">
                <del>原價 $1,499</del>
              </div>
            </div>
            <div className="product_btn">
              <button class="add_to_cart"><FontAwesomeIcon icon="cart-plus" />加入購物車</button>
              <button className="checkout_now">直接購買</button>
            </div>
          </div>
        </div>
        <div className="product_description">
          <div className="title">
            <h2>商品介紹</h2>
          </div>
          <div className="content">
            <p>「尋寶？致命詛咒？渺茫的機會？只要是跟這些有關的事，都算我一筆！」<br />
            一名無懼的年輕冒險家伊澤瑞爾的探險足跡遍布整個符文大陸，不論是多麼蠻荒偏遠之處，伊澤瑞爾都不會放過。在一趟前往古老蘇瑞瑪文明的探索之旅中，他在廢墟裡發現了不可思議的神秘力量。他發現了一個似乎是給霸權王者配戴的手鐲，他一戴上，那手鐲就緊緊地貼著他的手臂，讓他發出強大而令人不可置信的力量<br />
            超人氣公仔 伊澤瑞爾 身為英雄聯盟迷的你絕對不要錯過喔 趕快來入手吧 ^^</p>
          </div>
        </div>
      </div>
    </div>
  )
};

export default Product;