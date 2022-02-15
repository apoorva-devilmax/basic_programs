let arr = [
	{
		_id: new ObjectId("61ed73fc02496b164d9b190f"),
		imagePath: 'http://via.placeholder.com/200x200/grey?text=Product',
		title: 'Groceries',
		description: 'Get doorstep delivery now!',
		price: 209,
		__v: 0
	},
	{
		_id: new ObjectId("74328974289"),
		imagePath: 'http://via.placeholder.com/200x200/grey?text=Product',
		title: 'Groceries',
		description: 'Get doorstep delivery now!',
		price: 209,
		__v: 0
	}
]

let out_arr = arr.map(el => {
	el._id = el._id.toString()
});

console.log(out_arr)