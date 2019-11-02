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
        image={swiperProduct.image}
        name={swiperProduct.name}
        price={swiperProduct.special_price}
        originPrice={swiperProduct.original_price}
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
  return (
    <div className="collection_swiper">
      <Swiper {...params}>
        {swiperProducts}
      </Swiper>
    </div>
  );
};

export default CollectionSwiper;