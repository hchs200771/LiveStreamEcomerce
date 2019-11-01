import React from 'react';
import '../assets/scss/collection_product.scss'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

const CollectionProduct = (props) => {
  const {
    image,
    name,
    price,
    originPrice,
    id,
  } = props;

  const addCart = () => {
    const cart = JSON.parse(localStorage.getItem('cart')) || [];
    // check exist
    const alreadyExistProduct = cart.find(e => e.id === id);
    if (alreadyExistProduct) {
      cart.forEach(data => {
        data.quantity = alreadyExistProduct.quantity + 1
      })
    } else {
      cart.push({
        id,
        name,
        image,
        quantity: 1,
        special_price: price,
        original_price: originPrice,
      })
    }
    localStorage.setItem('cart', JSON.stringify(cart))
  }

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
          <button className="add_to_cart" onClick={addCart}>
            <FontAwesomeIcon icon="cart-plus" />
            加入購物車
          </button>
        </div>
      </div>
    </div>
  );
};

export default CollectionProduct;