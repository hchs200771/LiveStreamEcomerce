import React, { useContext, useState, useEffect } from 'react';
import Swiper from 'react-id-swiper';
import CollectionProduct from '../components/CollectionProduct';
import DataApi from '../api/DataApi'
import '../assets/scss/product.scss'
import { AppContext } from '../context/AppContext';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

const Product = (props) => {
  const { addCart } = useContext(AppContext);
  const [productData, setProductData] = useState(null);
  const [relatedProductsData, setRelatedProductsData] = useState([]);
  useEffect(() => {
    const getProduct =  async() => {
      const data = await DataApi.getProduct(props.match.params.id);
      let relatedProductsArray = [];
      data.category_collection.forEach(async (a) => {
        const relatedData = await DataApi.getCategoriesProducts(a.id);
        relatedProductsArray = relatedProductsArray.concat(relatedData.products);
        setRelatedProductsData(relatedProductsArray);
      });
      setProductData(data);
    }
    getProduct();
  }, [props]);

  const product_categories = productData && productData.category_collection.map(product_category => {
    return <a href={'/collection/' + product_category.id} key={product_category.id}>{product_category.name}</a>
  });

  const swiperProducts = relatedProductsData.map((swiperProduct) => {
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
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
  }

  return (
    <div id="product">
      <div className="container">
        <div className="row main_row">
          <div className="product_image col-md-6">
            <img src={productData && productData.image} />
          </div>
          <div className="product_info col-md-6">
            <div className="product_title">
              <h1>{productData && productData.name}</h1>
            </div>
            <div className="product_brief">
              <p>{productData && productData.brief}</p>
            </div>
            <div className="product_categories">
              {product_categories}
            </div>
            <div className="product_price row">
              <div className="onsale">
                <span>特價</span>
                <b>NT ${productData && productData.special_price}</b>
              </div>
              <div className="ori_price">
                <del>原價 ${productData && productData.original_price}</del>
              </div>
            </div>
            <div className="product_btn">
              <button className="add_to_cart" onClick={() => addCart(productData)}><FontAwesomeIcon icon="cart-plus" />加入購物車</button>
              <button className="checkout_now">直接購買</button>
            </div>
          </div>
        </div>
        <div className="product_description">
          <div className="title">
            <h3>商品介紹</h3>
          </div>
          <div className="content">
            <p dangerouslySetInnerHTML={{ __html: productData && productData.description }} />
          </div>
        </div>
        <div className="related_products">
          <h3>相關商品</h3>
          <div className="content">
            <Swiper {...params} shouldSwiperUpdate>
              {swiperProducts}
            </Swiper>
          </div>
        </div>
      </div>
    </div>
  )
};

export default Product;