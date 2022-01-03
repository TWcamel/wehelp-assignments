// # 1

function calculate(min, max) {
	let sum = 0
	for (let i = min; i <= max; ++i) sum += i
	console.log(sum)
}
calculate(1, 3); // 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8); // 你的程式要能夠計算 4+5+6+7+8，最後印出 30

// # 2

function avg(data) {
	let sum = 0
	data.employees.forEach(e => {
		sum += e.salary
	});
	const avg_salary = sum / data.count
	console.log(avg_salary)
}
avg({
	"count": 3,
	"employees": [
		{
			"name": "John",
			"salary": 30000
		},
		{
			"name": "Bob",
			"salary": 60000
		},
		{
			"name": "Jenny",
			"salary": 50000
		}
	]
}); // 呼叫 avg 函式


// # 3
function maxProduct(nums) {
	const len = nums.length
	let max = Number.MIN_SAFE_INTEGER
	for (let i = 0; i < len; ++i) {
		for (let j = i + 1; j < len; ++j) {
			let product = nums[i] * nums[j]
			if (product > max) max = product
		}
	}
	console.log(max)
}
maxProduct([5, 20, 2, 6]) // 得到 120
maxProduct([10, -20, 0, 3]) // 得到 30
maxProduct([-1, 2]) // 得到 -2
maxProduct([-1, 0, 2]) // 得到 0
maxProduct([-1, 0, -2]) // 得到 2


// # 4

function twoSum(nums, target) {
	const historyMap = new Map();
	let result = []
	nums.forEach((num, index) => {
		let remaining = target - num
		if (historyMap.has(remaining)) {
			result.push(historyMap.get(remaining))
			result.push(index)
		}
		else {
			historyMap.set(num, index)
		}
	})
	return result
}
let result = twoSum([2, 11, 7, 15], 9);
console.log(result); // show [0, 2] because nums[0]+nums[2] is 9

// # 5
function maxZeros(nums) {
	maxCount = 0
	count = 0
	for (let i = 0; i < nums.length; ++i) {
		if (nums[i] === 0) count++
		else count = 0
		if (count > maxCount) maxCount = count
	}
	console.log(maxCount)

}
maxZeros([0, 1, 0, 0]); // 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]); // 得到 4
maxZeros([1, 1, 1, 1, 1]); // 得到 0
maxZeros([0, 0, 0, 1, 1]) // 得到 3