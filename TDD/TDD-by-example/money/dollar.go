package money

type Dollar struct {
	Money
}

func (d *Dollar) Times(multiplier int) *Dollar {
	return NewDollar(d.amount * multiplier)
}
func (d *Dollar) Equals(other any) bool {
	otherDollar, ok := other.(*Dollar)
	return ok && d.amount == otherDollar.amount
}
func NewDollar(amount int) *Dollar {
	return &Dollar{
		Money: Money{amount: amount},
	}
}
