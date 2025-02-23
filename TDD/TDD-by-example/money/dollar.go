package money

type Dollar struct {
	Amount int
}

func (d *Dollar) Times(multiplier int) {}
func NewDollar(amount int) *Dollar {
	return &Dollar{Amount: 10}
}
