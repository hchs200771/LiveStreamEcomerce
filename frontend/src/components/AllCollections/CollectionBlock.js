import React from 'react';
import CollectionSwiper from './CollectionSwiper'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import '../../assets/scss/all_collections.scss';

const CollectionBlock = (props) => {
  const {
    id,
    title,
    productsData,
    collectionUrl,
  } = props;
  return (
    <div className="collection_block" id={id}>
      <div className="collection_head">
        <h2>{title}</h2>
        <div className="see_more">
          <a href={collectionUrl}>看更多<FontAwesomeIcon icon="angle-double-right" /></a>
        </div>
      </div>
      <CollectionSwiper
        productsData={productsData}
      />
    </div>
  );
};

export default CollectionBlock;