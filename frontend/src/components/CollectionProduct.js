import React from 'react';
import '../assets/scss/collection_product.scss'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

const CollectionProduct = (props) => {
  const {
    imgUrl,
    name,
    price,
    originPrice,
    id,
  } = props;
  return (
    <div className="product swiper-slide">
      <div className="product_image">
        <img src={imgUrl} />
        <a href={'/products/' + id}>
          <span>
            <FontAwesomeIcon icon="search" />
            查看商品
          </span>
        </a>
      </div>
      <div className="caption">
        <div className="product_title">
          <h2>{name}</h2>
        </div>
        <div className="product_price">
          <b className="price">特價 ${price}</b>
          <span className="origin_price">原價 ${originPrice}</span>
        </div>
        <div class="product_btn">
          <button class="add_to_cart"><FontAwesomeIcon icon="cart-plus" />加入購物車</button>
        </div>
      </div>
    </div>
  );
};

export default CollectionProduct;