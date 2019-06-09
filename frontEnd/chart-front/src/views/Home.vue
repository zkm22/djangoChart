<template>
  <div id="home">
    <div class="chart-wrapper">
      <highcharts-component :options="options" :styles="styles" ref="simpleChart"></highcharts-component>
    </div>
    <loading :loading="!ready||saving"></loading>
    <button :disabled="!ready" @click="saveToTable2">Save</button>
  </div>
</template>

<script>
// @ is an alias to /src
import HighchartsComponent from '@/components/HighchartsComponent.vue'
import Loading from '@/components/Loading.vue'

export default {
  name: 'home',
  components: {
    HighchartsComponent,
    Loading
  },
  data () {
    return {
      data1: [],
      data2: [],
      ready: false,
      saving: false,
      options: {
        chart: {
          type: 'column'
        },
        title: {
          text: 'Table1'
        },
        xAxis: {
          categories: [
            'nth0',
            'nth1',
            'nth2',
            'nth3',
            'nth4',
            'nth5',
            'nth6',
            'nth7',
            'nth8',
            'nth9'
          ]
        },
        yAxis: {
          title: {
            text: 'Value'
          },
          lineWidth: 2,
          lineColor: '#F33',
          id: 'table1-axis'
        },
        series: [{
          name: 'area1',
          color: 'green'
        }, {
          name: 'area2',
          color: 'red'
        }]
      },
      styles: {
        width: 600,
        height: 400
      },
      intv: null,
      pending: false
    }
  },
  methods: {
    getDataFromSourse1 () {
      return this.axios({
        url: `/chartApi/getData1`,
        method: 'get'
      })
    },
    getDataFromSourse2 () {
      return this.axios({
        url: `/chartApi/getData2`,
        method: 'get'
      })
    },
    getCSRFToken () {
      return document.getElementsByName('csrfmiddlewaretoken')[0].value
    },
    saveToTable2 () {
      this.saving = true
      let dataList = []
      for (let i = 0; i < 10; ++i) {
        dataList.push({
          area1: this.data1[i].value,
          area2: this.data2[i].value,
          nth: i
        })
      }
      console.log(dataList)
      this.axios({
        url: `/chartApi/saveToTable2`,
        method: 'post',
        headers: {
          'X-CSRFToken': this.token
        },
        data: {
          dataList
        }
      }).then(res => {
        console.log(res)
        this.saving = false
      }).catch(err => {
        console.warn(err)
        this.saving = false
      })
    },
    getData () {
      if (!this.pending) {
        this.pending = true
        this.axios.all([
          this.getDataFromSourse1(),
          this.getDataFromSourse2()
        ]).then(this.axios.spread((data1, data2) => {
          let data1List = data1.data
          let data2List = data2.data
          let sortData1 = data1List.sort((a, b) => {
            return a.nth - b.nth
          })
          let sortData2 = data2List.sort((a, b) => {
            return a.nth - b.nth
          })
          this.sessionStorage.save('data1', sortData1)
          this.sessionStorage.save('data2', sortData2)
          this.data1 = sortData1
          this.data2 = sortData2
          let dataList = []
          for (let item of sortData1) {
            dataList.push(item.value)
          }
          this.$refs.simpleChart.chart.series[0].setData(dataList)
          dataList = []
          for (let item of sortData2) {
            dataList.push(item.value)
          }
          this.$refs.simpleChart.chart.series[1].setData(dataList)
          this.ready = true
          this.pending = false
        })).catch(err => {
          console.warn(err)
          this.pending = false
        })
      }
    }
  },
  created () {
    this.token = this.getCSRFToken()
    let data1 = this.sessionStorage.fetch('data1')
    let data2 = this.sessionStorage.fetch('data2')
    if (data1 && data2) {
      this.data1 = data1
      this.data2 = data2
      let dataList1 = []
      let dataList2 = []
      for (let item of data1) {
        dataList1.push(item.value)
      }
      this.$nextTick(_ => {
        this.$refs.simpleChart.chart.series[0].setData(dataList1)
      })
      for (let item of data2) {
        dataList2.push(item.value)
      }
      this.$nextTick(_ => {
        this.$refs.simpleChart.chart.series[1].setData(dataList2)
      })
      this.ready = true
    } else {
      this.getData()
    }
    this.intv = setInterval(_ => {
      this.getData()
    }, 10000)
  },
  beforeDestroy () {
    clearInterval(this.intv)
  }
}
</script>
<style lang="scss" scoped>
.chart-wrapper {
  width: 100%;
  display: flex;
  justify-content: center;
  margin-top: 20px;
}
</style>