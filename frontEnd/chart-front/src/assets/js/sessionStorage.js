export default {
  fetch: function (key) {
    let item = window.sessionStorage.getItem(key)
    if (item != 'undefined') {
      return window.JSON.parse(item)
    }
    return null
  },
  save: function (key, item) {
    window.sessionStorage.setItem(key, window.JSON.stringify(item))
  },
  delete: function (key) {
    window.sessionStorage.removeItem(key)
  }
}
