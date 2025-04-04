<template>
  <div>
    <h2>API de busca operadoras</h2>
    <input type="text" v-model="termoBusca" placeholder="Digite o nome..." />
    <button @click="buscarOperadoras">Buscar</button>

    <ul v-if="operadoras.length">
      <li v-for="operadora in operadoras" :key="operadora.Registro_ANS">
        <strong>{{ operadora.Razao_Social }}</strong> - {{ operadora.Nome_Fantasia }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      termoBusca: '',
      operadoras: []
    };
  },
  methods: {
    async buscarOperadoras() {
      if (this.termoBusca.length < 2) return;
      const response = await axios.get(`http://127.0.0.1:8000/buscar-operadoras/?termo=${this.termoBusca}`);
      this.operadoras = response.data;
    }
  }
};
</script>