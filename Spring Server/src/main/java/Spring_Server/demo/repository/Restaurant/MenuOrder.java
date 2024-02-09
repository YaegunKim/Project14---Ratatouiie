// import javax.persistence.*;

// @Entity
// public class MenuOrder {
//     @Id
//     @GeneratedValue(strategy = GenerationType.AUTO)
//     private Long id;

//     private String menuItem;
//     private double price;

//     @ManyToOne
//     @JoinColumn(name = "table_id")
//     private RestaurantTable table;

//     // Getters and Setters
//     public Long getId() {
//         return id;
//     }

//     public void setId(Long id) {
//         this.id = id;
//     }

//     public String getMenuItem() {
//         return menuItem;
//     }

//     public void setMenuItem(String menuItem) {
//         this.menuItem = menuItem;
//     }

//     public double getPrice() {
//         return price;
//     }

//     public void setPrice(double price) {
//         this.price = price;
//     }

//     public RestaurantTable getTable() {
//         return table;
//     }

//     public void setTable(RestaurantTable table) {
//         this.table = table;
//     }
// }
