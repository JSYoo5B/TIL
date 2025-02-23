package money

type Dollar struct {
	Amount int
}

func (d *Dollar) Times(multiplier int) *Dollar {
	return &Dollar{Amount: d.Amount * multiplier}
}
func (d *Dollar) Equals(other any) bool {
	otherDollar, ok := other.(*Dollar)
	return ok && d.Amount == otherDollar.Amount
}
func NewDollar(amount int) *Dollar {
	return &Dollar{Amount: amount}
}
