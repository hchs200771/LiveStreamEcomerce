import React, { useContext } from 'react';
import '../assets/scss/collection_product.scss'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { AppContext } from '../context/AppContext';

const CollectionProduct = (props) => {
  const { addCart } = useContext(AppContext)
  const {
    image,
    name,
    price,
    originPrice,
    id,
  } = props;

  return (
    <div className="product swiper-slide">
      <div className="product_image">
        <img src={image} />
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
        <div className="product_btn">
          <button className="add_to_cart" onClick={() => addCart({id, name, image, price, originPrice})}>
            <FontAwesomeIcon icon="cart-plus" />
            加入購物車
          </button>
        </div>
      </div>
    </div>
  );
};

export default CollectionProduct;