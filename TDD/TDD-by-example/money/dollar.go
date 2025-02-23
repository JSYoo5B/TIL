package money

type Dollar struct {
	Amount int
}

func (d *Dollar) Times(multiplier int) *Dollar {
	return &Dollar{Amount: d.Amount * multiplier}
}
func NewDollar(amount int) *Dollar {
	return &Dollar{Amount: amount}
}
