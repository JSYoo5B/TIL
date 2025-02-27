package money

type Expression interface {
	Reduce(bank *Bank, to string) Money
	Plus(addend Expression) Expression
	Times(multiplier int) Expression
}

type Sum struct {
	Augend Expression
	Addend Expression
}

func (s *Sum) Reduce(bank *Bank, to string) Money {
	amount := s.Augend.Reduce(bank, to).getAmount() +
		s.Addend.Reduce(bank, to).getAmount()
	return newMoney(amount, to)
}
func (s *Sum) Plus(addend Expression) Expression {
	return NewSum(s, addend)
}
func (s *Sum) Times(multiplier int) Expression {
	return NewSum(s.Augend.Times(multiplier), s.Addend.Times(multiplier))
}

func NewSum(augend, addend Expression) *Sum {
	return &Sum{
		Augend: augend,
		Addend: addend,
	}
}
