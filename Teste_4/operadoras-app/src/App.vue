<template>
  <div id="app">
    <h1>Consulta de Operadoras</h1>
    <OperadoraSearch />
  </div>
</template>

<script>
import OperadoraSearch from "./components/OperadoraSearch.vue";

export default {
  components: {
    OperadoraSearch
  }
};
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
