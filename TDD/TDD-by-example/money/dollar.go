package money

type Dollar struct {
	amount int
}

func (d *Dollar) Times(multiplier int) *Dollar {
	return &Dollar{amount: d.amount * multiplier}
}
func (d *Dollar) Equals(other any) bool {
	otherDollar, ok := other.(*Dollar)
	return ok && d.amount == otherDollar.amount
}
func NewDollar(amount int) *Dollar {
	return &Dollar{amount: amount}
}
