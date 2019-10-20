import React from 'react';

const CollectionSwiperProduct = (props) => {
  const {
    imgUrl,
    name,
    price,
    originPrice,
    productHandle,
  } = props;
  return (
    <div className="swiper_product swiper-slide">
      <div className="product_image">
        <a href={productHandle}><img src={imgUrl} /></a>
      </div>
      <div className="caption">
        <div className="product_title">
          <h2>{name}</h2>
        </div>
        <div className="product_price">
          <b className="price">特價 ${price}</b>
          <span className="origin_price">原價 ${originPrice}</span>
        </div>
      </div>
    </div>
  );
};

export default CollectionSwiperProduct;