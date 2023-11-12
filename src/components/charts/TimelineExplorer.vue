<!-- Developed by Taipei Urban Intelligence Center 2023 -->

<script setup>
import { ref, computed } from "vue";
import { useMapStore } from "../../store/mapStore";

const props = defineProps([
	"chart_config",
	"activeChart",
	"series",
	"map_config",
]);
const mapStore = useMapStore();

const chartOptions = ref({
	chart: {
		offsetY: 15,
		stacked: true,
		toolbar: {
			show: false,
		},
	},
	colors: props.chart_config.color,
	dataLabels: {
		offsetX: 20,
		textAnchor: "start",
	},
	grid: {
		show: false,
	},
	legend: {
		show: false,
	},
	plotOptions: {
		bar: {
			borderRadius: 2,
			distributed: true,
			horizontal: true,
		},
	},
	stroke: {
		colors: ["#282a2c"],
		show: true,
		width: 0,
	},
	// The class "chart-tooltip" could be edited in /assets/styles/chartStyles.css
	tooltip: {
		custom: function ({ series, seriesIndex, dataPointIndex, w }) {
			return (
				'<div class="chart-tooltip">' +
				"<h6>" +
				w.globals.labels[dataPointIndex] +
				"</h6>" +
				"<span>" +
				series[seriesIndex][dataPointIndex] +
				` ${props.chart_config.unit}` +
				"</span>" +
				"</div>"
			);
		},
		followCursor: true,
	},
	xaxis: {
		axisBorder: {
			show: false,
		},
		axisTicks: {
			show: false,
		},
		labels: {
			show: false,
		},
		type: "category",
	},
	yaxis: {
		labels: {
			formatter: function (value) {
				return value.length > 7 ? value.slice(0, 6) + "..." : value;
			},
		},
	},
});

const chartHeight = computed(() => {
	return `${40 + props.series[0].data.length * 24}`;
});

const selectedIndex = ref(null);

function handleDataSelection(e, chartContext, config) {
	if (!props.chart_config.map_filter) {
		return;
	}
	if (config.dataPointIndex !== selectedIndex.value) {
		mapStore.addLayerFilter(
			`${props.map_config[0].index}-${props.map_config[0].type}`,
			props.chart_config.map_filter[0],
			props.chart_config.map_filter[1][config.dataPointIndex]
		);
		selectedIndex.value = config.dataPointIndex;
	} else {
		mapStore.clearLayerFilter(
			`${props.map_config[0].index}-${props.map_config[0].type}`
		);
		selectedIndex.value = null;
	}
}
</script>

<template>
	<div v-if="activeChart === 'TimelineExplorer'">
		<div class="activity-detail">
			<div class="activity-name">2023繽紛耶誕玩台北｜北投區</div>
			<div class="activity-date">2023-11-17 ~ 2024-01-01</div>
		</div>

		<div class="activity-detail">
			<div class="activity-name">2023繽紛耶誕玩台北｜北投區</div>
			<div class="activity-date">2023-11-17 ~ 2024-01-01</div>
		</div>

		<div class="activity-detail">
			<div class="activity-name">2023繽紛耶誕玩台北｜北投區</div>
			<div class="activity-date">2023-11-17 ~ 2024-01-01</div>
		</div>

		<div class="activity-detail">
			<div class="activity-name">2023繽紛耶誕玩台北｜北投區</div>
			<div class="activity-date">2023-11-17 ~ 2024-01-01</div>
		</div>

		<div class="activity-detail">
			<div class="activity-name">2023繽紛耶誕玩台北｜北投區</div>
			<div class="activity-date">2023-11-17 ~ 2024-01-01</div>
		</div>
	</div>
</template>

<style scoped lang="scss">
.activity {
	&-detail {
		padding: calc(var(--font-m) / 2);
		background-color: #4d4d4d;
		border-radius: 5px;
		margin: 12px 5px;
	}
	&-name {
		margin-bottom: calc(var(--font-m) / 4);
	}
	&-date {
		font-size: var(--font-s);
	}
}
</style>
