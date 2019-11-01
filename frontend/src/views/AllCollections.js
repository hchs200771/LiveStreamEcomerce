import React, {useState, useEffect} from 'react';
import CollectionBlock from '../components/AllCollections/CollectionBlock';
import DataApi from '../api/DataApi'

import '../assets/scss/all_collections.scss';

const AllCollections = (props) => {
  const [allCollections, setAllCollections] = useState(null);
  useEffect(() => {
    
    const getAllCategoriesProducts = async () => {
      const data = await DataApi.getAllCategoriesProducts(props.match.params.id)
      setAllCollections(data)
    }
    getAllCategoriesProducts()
  }, [props])
  
  const collections = allCollections && allCollections.map((collection) => {
    return (
      <CollectionBlock
        key={collection.id}
        id={collection.id}
        title={collection.name}
        productsData={collection.products}
        collectionUrl={collection.id}
      />
    )
  });

  return (
    <div id="all_collections">
      <div className="container">
        {collections}
      </div>
    </div>
  );
}

export default AllCollections;