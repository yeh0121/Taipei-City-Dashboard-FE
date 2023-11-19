<script setup>
import { ref, onMounted, watch } from "vue";

const props = defineProps([
	"chart_config",
	"activeChart",
	"series",
	"map_config",
]);

const rangeLimit = ref({
	minYear: 0,
	maxYear: 0,
});

const yearArray = [];

props.series[0].data.forEach((year) => {
	yearArray.push(parseInt(year.x));
});
rangeLimit.value.minYear = Math.min(...yearArray);
rangeLimit.value.maxYear = Math.max(...yearArray);

const currentTime = ref("");

onMounted(() => {
	const getCurrentTime = () => {
		const currentDate = new Date();
		currentTime.value = currentDate.getTime(); // 可以根据需要调整时间格式
	};
	getCurrentTime();

	return {
		currentTime,
	};
});

const date1 = ref(rangeLimit.value.minYear);
const date2 = ref(rangeLimit.value.maxYear);
date1.value = currentTime.value;

const minRange = ref(rangeLimit.value.minYear);
const maxRange = ref(rangeLimit.value.maxYear);

const updateSliderValue1 = (event) => {
	minRange.value = event.target.value;
};

const updateSliderValue2 = (event) => {
	maxRange.value = event.target.value;
};

watch(minRange, (newValue) => {
	if (minRange.value < maxRange.value) {
		date1.value = newValue;
		//min
		console.log("Slider 1 value:", newValue, 73);
	} else {
		date2.value = newValue;
		console.log("Slider 1 value:", newValue, 76);
	}
});
watch(maxRange, (newValue) => {
	if (minRange.value < maxRange.value) {
		date2.value = newValue;
		//max
		console.log("Slider 2 value:", newValue, 81);
	} else {
		date1.value = newValue;
		console.log("Slider 2 value:", newValue, 85);
	}
});
</script>

<template>
	<div v-if="activeChart === 'TimelineExplorer'">
		<div class="flex" style="padding-top: 16px; position: relative">
			<input
				id="range-btn-1"
				class="range-btn range-btn-1"
				type="range"
				v-model="minRange"
				@input="updateSliderValue1"
				:min="rangeLimit.minYear"
				:max="rangeLimit.maxYear"
				step="1"
				style="width: 100%"
			/>
			<input
				id="range-btn-2"
				class="range-btn range-btn-2"
				type="range"
				v-model="maxRange"
				@input="updateSliderValue2"
				:min="rangeLimit.minYear"
				:max="rangeLimit.maxYear"
				step="1"
				style="width: 100%"
			/>
		</div>
		<div class="timeline-bg"></div>
		<div class="flex" style="justify-content: center; margin-top: 5px">
			<div>
				<input type="text" v-model="date1" style="width: 36px" />年 ～
			</div>

			<div>
				<input type="text" v-model="date2" style="width: 36px" />年
			</div>
		</div>

		<div class="activity">
			<div v-for="(serie, index) in series[0].data" :key="index">
				<div
					v-if="serie.x >= date1 && serie.x <= date2"
					class="activity-detail"
				>
					<div class="activity-name">
						{{ serie.x }}年｜{{ serie.y }}
					</div>
					<div class="activity-date">{{ serie.z }}</div>
				</div>
			</div>
		</div>
	</div>
</template>

<style scoped lang="scss">
.activity {
	font-size: var(--font-s);

	&-detail {
		padding: calc(var(--font-m) / 2);
		background-color: #4d4d4d;
		border-radius: 5px;
		margin: 6px 0px;
	}
	&-name {
		margin-bottom: calc(var(--font-m) / 4);
	}
	&-date {
		font-size: var(--font-s);
	}
}

.range-btn {
	border-radius: 5px;
	top: 0;
	left: 0;
	outline: none;
	appearance: none;
	border: none;
	padding: 0;
	position: absolute;
	&-1 {
		left: 0;
	}
	&-2 {
		right: 0;
	}
	&::-webkit-slider-thumb {
		-webkit-appearance: none;
		appearance: none;
		width: 16px;
		height: 16px;
		background-image: url("../../../public/images/thumbnails/triangle-filled.svg");
		background-size: cover;
		border-radius: 50%;
		cursor: pointer;
	}
}

[type="range"] {
	pointer-events: none;
	&::-webkit-slider-runnable-track {
		background: none;
	}
	&::-webkit-slider-thumb {
		pointer-events: auto;
		&::-moz-range-thumb {
			pointer-events: auto;
		}
	}
}

.timeline > input {
	position: absolute;
	top: 0;
	left: 0;
}

.timeline-bg {
	background: #6dd3ff;
	width: 100%;
	height: 8px;
	border-radius: 5px;
}
.flex {
	display: flex;
}
</style>
