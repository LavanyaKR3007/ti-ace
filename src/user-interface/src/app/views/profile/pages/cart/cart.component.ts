import { Component, OnInit } from '@angular/core';
import { CartService } from 'src/app/services/cart.service';

@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.scss']
})
export class CartComponent implements OnInit {
  cartItems: any;
  constructor(private readonly cartService: CartService) {
    this.cartItems = this.cartService.cartItems;
  }

  ngOnInit(): void {
  }
}
