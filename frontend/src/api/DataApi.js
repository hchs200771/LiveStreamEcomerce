import api from './Setting';

export default {
  getCategories() {
    return api.execute('get', '/categories');
  },
  getCategoriesProducts(id) {
    return api.execute('get', `/categories/${id}?with_product=1`);
  },
  getAllCategoriesProducts() {
    return api.execute('get', `/categories?with_product=1`);
  },
  createOrder(data) {
    return api.execute('post', '/orders', data)
  },
  getOrderInfo(id) {
    return api.execute('get', `/orders/${id}`)
  }
}
