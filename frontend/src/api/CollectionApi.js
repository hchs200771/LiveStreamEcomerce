import api from './Setting';

export default {
  getCategories() {
    return api.execute('get', '/categories');
  },
}
