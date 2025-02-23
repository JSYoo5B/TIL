package money

type Franc struct {
	Money
}

func (f *Franc) Times(multiplier int) *Franc {
	return NewFranc(f.amount * multiplier)
}
func (f *Franc) Equals(other any) bool {
	otherFranc, ok := other.(*Franc)
	return ok && f.amount == otherFranc.amount
}
func NewFranc(amount int) *Franc {
	return &Franc{
		Money: Money{amount},
	}
}
