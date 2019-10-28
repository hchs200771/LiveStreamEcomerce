import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { library } from '@fortawesome/fontawesome-svg-core';
// import { fab } from '@fortawesome/free-brands-svg-icons';
import {
  faShoppingCart,
  faAngleDoubleRight,
  faCartPlus,
} from '@fortawesome/free-solid-svg-icons';

import './assets/scss/theme.scss';

import Header from './components/Header';
import Footer from './components/Footer';
import AllCollections from './views/AllCollections';
import Collection from './views/Collection';
import Product from './views/Product';

library.add(
  faShoppingCart,
  faAngleDoubleRight,
  faCartPlus
);

function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <Header />
        <Switch>
          <Route exact path="/" component={AllCollections} />
          <Route path="/collection/:id" component={Collection} />
          <Route path="/products/:id" component={Product} />
        </Switch>
        <Footer />
      </div>
    </BrowserRouter>
  );
}

export default App;
