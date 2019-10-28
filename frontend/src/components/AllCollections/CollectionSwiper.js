import React from 'react';
import Swiper from 'react-id-swiper';
import CollectionProduct from '../CollectionProduct';

const CollectionSwiper = (props) => {
  const {
    productsData,
  } = props;
  const swiperProducts = productsData.map((swiperProduct) => {
    return (
      <CollectionProduct
        key={swiperProduct.id}
        imgUrl={swiperProduct.imgUrl}
        name={swiperProduct.name}
        price={swiperProduct.price}
        originPrice={swiperProduct.originPrice}
        productHandle={swiperProduct.productHandle}
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
  return (
    <div className="collection_swiper">
      <Swiper {...params}>
        {swiperProducts}
      </Swiper>
    </div>
  );
};

export default CollectionSwiper;