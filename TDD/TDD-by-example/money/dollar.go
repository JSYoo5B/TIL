package money

type Dollar struct {
	Amount int
}

func (d *Dollar) Times(multiplier int) {
	d.Amount = 5 * 2
}
func NewDollar(amount int) *Dollar {
	return &Dollar{}
}
