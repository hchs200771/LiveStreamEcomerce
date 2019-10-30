import React from 'react';
import Swiper from 'react-id-swiper';
import CollectionProduct from '../components/CollectionProduct';
import '../assets/scss/product.scss'

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

const productData = {
  id: 2,
  name: "英雄聯盟LOL 吉茵珂絲公仔 暴走蘿莉大炮戰鬥版大號模型",
  brief: "超人氣角色 吉茵珂絲公仔 數量有限要買要快喔~",
  description: "尺寸:26CM<br /><br />材質：PVC<br />包裝方式：彩盒包裝<br />交期為七個工作日  下單前請參考 賣場簡介<br />圖片為官方圖片，僅供参考，請以實物為準。<br />PVC模型等商品屬於工廠大量製造之商品，如有輕微溢色、輕微掉漆等小瑕疵，<br />皆屬於正常狀況。不接受以此為理由的退換貨，對質料有強烈要求者，建議前往實體店面選購您心目中理想的喜愛的商品。",
  image: "http://gw3.alicdn.com/bao/uploaded/i3/TB1vBQYKpXXXXX.XVXXXXXXXXXX_!!0-item_pic.jpg",
  category_collection: [
    {
      id: 1,
      name: "英雄聯盟",
    },
    {
      id: 2,
      name: "熱門公仔",
    },
  ],
  price: "999",
  ori_price: "1,499",
};

const {
  id,
  name,
  brief,
  description,
  image,
  category_collection,
  price,
  ori_price,
} = productData;

const current_cate_pd_1 = [
  {
    id: 1,
    name: "英雄聯盟 世界大賽官方正版公仔 脈衝火焰 伊澤瑞爾",
    brief: "EZREAL",
    description: "ezreal",
    image: "https://cf.shopee.tw/file/ad118a574093b7d6ccbe469bfd0ec3a1",
    category_collection: [
      {
        id: 1,
        name: "英雄聯盟"
      }
    ],
    price: 999
  },
  {
    id: 2,
    name: "英雄聯盟LOL 吉茵珂絲公仔 暴走蘿莉大炮戰鬥版大號模型",
    brief: "JINX",
    description: "jinx",
    image: "http://gw3.alicdn.com/bao/uploaded/i3/TB1vBQYKpXXXXX.XVXXXXXXXXXX_!!0-item_pic.jpg",
    category_collection: [
      {
        id: 1,
        name: "英雄聯盟"
      },
      {
        id: 2,
        name: "熱門公仔"
      },
    ],
    price: 999
  }, 
];
const current_cate_pd_2 = [
  {
    id: 3,
    name: "英雄聯盟 世界大賽官方正版公仔 艾希",
    brief: "Ashe",
    description: "ashe",
    image: "https://img.ruten.com.tw/s2/3/74/c8/21822100524232_188.jpg",
    category_collection: [
      {
        id: 1,
        name: "熱門公仔"
      }
    ],
    price: 999
  },
];
productData.category_collection.forEach(()=> {
  
});
const related_products = current_cate_pd_1.concat(current_cate_pd_2);

const swiperProducts = related_products.map((swiperProduct) => {
  return (
    <CollectionProduct
      key={swiperProduct.id}
      image={swiperProduct.image}
      name={swiperProduct.name}
      price={swiperProduct.price}
      originPrice={swiperProduct.originPrice}
      id={swiperProduct.id}
    />
  );
});
const params = {
  slidesPerView: 4,
  spaceBetween: 16,
  pagination: {
    el: '.swiper-pagination',
    type: 'bullets',
    clickable: true,
  },
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
}

const Product = () => {
  return (
    <div id="product">
      <div className="container">
        <div className="row">
          <div className="product_image col-md-6">
            <img src={image} />
          </div>
          <div className="product_info col-md-6">
            <div className="product_title">
              <h1>{name}</h1>
            </div>
            <div className="product_brief">
              <p>{brief}</p>
            </div>
            <div className="product_price row">
              <div className="onsale">
                <span>特價</span>
                <b>NT ${price}</b>
              </div>
              <div className="ori_price">
                <del>原價 ${ori_price}</del>
              </div>
            </div>
            <div className="product_btn">
              <button className="add_to_cart"><FontAwesomeIcon icon="cart-plus" />加入購物車</button>
              <button className="checkout_now">直接購買</button>
            </div>
          </div>
        </div>
        <div className="product_description">
          <div className="title">
            <h3>商品介紹</h3>
          </div>
          <div className="content">
            <p>{description}</p>
          </div>
        </div>
        <div className="related_products">
          <h3>相關商品</h3>
          <div className="content">
            <Swiper {...params}>
              {swiperProducts}
            </Swiper>
          </div>
        </div>
      </div>
    </div>
  )
};

export default Product;