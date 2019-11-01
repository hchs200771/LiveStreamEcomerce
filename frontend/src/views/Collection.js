import React, { useState, useEffect } from 'react';
import CollectionProduct from '../components/CollectionProduct'
import banner from '../assets/img/avengers.jpg'
import DataApi from '../api/DataApi'

import '../assets/scss/collection.scss'

const Collection = (props) => {
  const [allCollections, setAllCollections] = useState([]);
  const [collectionData, setCollectionData] = useState(null);

  useEffect(() => {
    const getCategories = async () => {
      const data = await DataApi.getCategories()
      setAllCollections(data)
    }
    getCategories()
    
    const getCategoriesProducts = async () => {
      const data = await DataApi.getCategoriesProducts(props.match.params.id)
      setCollectionData(data)
    }
    getCategoriesProducts()
  }, [props])

  const products = collectionData && collectionData.products.map(product => {
    return (
      <div className="col-lg-4 col-md-6" key={product.id}>
        <CollectionProduct
          image={product.image}
          name={product.name}
          price={product.special_price}
          originPrice={product.original_price}
          id={product.id}
        />
      </div>
    );
  });

  return (
    <div id="collection">
      <div className="container">
        <div className="collection_banner">
          <img src={banner} />
        </div>
        <div className="row">
          <div className="side_menu col-lg-3 col-md-4">
            <div className="head">分類選單</div>
            <ul>
              {
                allCollections && allCollections.map( allCollection => {
                  return (
                    <li key={allCollection.id}>
                      <a className={collectionData && allCollection.id == collectionData.id ? 'active': ''} href={allCollection.id}>{allCollection.name}</a>
                    </li>
                  )
                })
              }
            </ul>
          </div>
          <div className="col-lg-9 col-md-8">
            <div className="head">{collectionData && collectionData.name}</div>
            <div className="products row">
              {products}
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Collection;