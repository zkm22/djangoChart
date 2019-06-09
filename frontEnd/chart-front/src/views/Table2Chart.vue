<template>
  <div id="table2-chart">
    <div class="chart-wrapper">
      <highcharts-component :options="options" :styles="styles" ref="simpleChart"></highcharts-component>
    </div>
    <loading :loading="!ready"></loading>
  </div>
</template>
<script>
import HighchartsComponent from '@/components/HighchartsComponent.vue'
import Loading from '@/components/Loading.vue'

export default {
  name: 'table2',
  components: {
    HighchartsComponent,
    Loading
  },
  data () {
    return {
      ready: false,
      options: {
        chart: {
          type: 'column'
        },
        title: {
          text: 'Table2'
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
            text: 'TotalValue'
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
      }
    }
  },
  methods: {
    getTable2Data () {
      this.axios({
        url: '/chartApi/getTable2Data',
        methods: 'get'
      }).then(res => {
        let data = res.data
        let area1 = []
        let area2 = []
        data.forEach(item => {
          if (area1[item.nth]) {
            area1[item.nth] += item.area1
          } else {
            area1[item.nth] = item.area1
          }
          if (area2[item.nth]) {
            area2[item.nth] += item.area2
          } else {
            area2[item.nth] = item.area2
          }
        })
        console.log(area1, area2)
        this.$nextTick(_ => {
          this.$refs.simpleChart.chart.series[0].setData(area1)
          this.$refs.simpleChart.chart.series[1].setData(area2)
        })
        this.ready = true
      }).catch(err => {
        console.warn(err)
        this.ready = true
      })
    }
  },
  created() {
    this.getTable2Data()
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
