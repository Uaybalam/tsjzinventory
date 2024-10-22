-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 22-10-2024 a las 20:36:46
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `controlinventario`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categoria`
--

CREATE TABLE `categoria` (
  `id_categoria` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `descripcion` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estado`
--

CREATE TABLE `estado` (
  `id_estado` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inventario`
--

CREATE TABLE `inventario` (
  `id_inventario` int(11) NOT NULL,
  `id_producto_sku` int(11) DEFAULT NULL,
  `cantidad` int(11) NOT NULL,
  `fecha_actualizacion` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productolpn`
--

CREATE TABLE `productolpn` (
  `id_producto_lpn` int(11) NOT NULL,
  `id_producto_sku` int(11) DEFAULT NULL,
  `id_ubicacion` int(11) DEFAULT NULL,
  `id_estado` int(11) DEFAULT NULL,
  `id_resguardante` int(11) DEFAULT NULL,
  `id_responsable` int(11) DEFAULT NULL,
  `fecha_actualizacion` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productosku`
--

CREATE TABLE `productosku` (
  `id_producto_sku` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `descripcion` text DEFAULT NULL,
  `id_categoria` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `resguardante`
--

CREATE TABLE `resguardante` (
  `id_resguardante` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `descripcion` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `responsable`
--

CREATE TABLE `responsable` (
  `id_responsable` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `descripcion` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `transaccion`
--

CREATE TABLE `transaccion` (
  `id_transaccion` int(11) NOT NULL,
  `id_producto_lpn` int(11) DEFAULT NULL,
  `tipo_transaccion` enum('Entrada','Salida','Actualización') NOT NULL,
  `descripcion` text DEFAULT NULL,
  `fecha_transaccion` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ubicacion`
--

CREATE TABLE `ubicacion` (
  `id_ubicacion` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `descripcion` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id_usuario` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `contrasena` varchar(255) NOT NULL,
  `rol` enum('Administrador','Responsable','Usuario') NOT NULL,
  `fecha_creacion` datetime DEFAULT current_timestamp(),
  `estado` enum('Activo','Inactivo') DEFAULT 'Activo'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `categoria`
--
ALTER TABLE `categoria`
  ADD PRIMARY KEY (`id_categoria`);

--
-- Indices de la tabla `estado`
--
ALTER TABLE `estado`
  ADD PRIMARY KEY (`id_estado`);

--
-- Indices de la tabla `inventario`
--
ALTER TABLE `inventario`
  ADD PRIMARY KEY (`id_inventario`),
  ADD KEY `id_producto_sku` (`id_producto_sku`);

--
-- Indices de la tabla `productolpn`
--
ALTER TABLE `productolpn`
  ADD PRIMARY KEY (`id_producto_lpn`),
  ADD KEY `id_producto_sku` (`id_producto_sku`),
  ADD KEY `id_ubicacion` (`id_ubicacion`),
  ADD KEY `id_estado` (`id_estado`),
  ADD KEY `id_resguardante` (`id_resguardante`),
  ADD KEY `id_responsable` (`id_responsable`);

--
-- Indices de la tabla `productosku`
--
ALTER TABLE `productosku`
  ADD PRIMARY KEY (`id_producto_sku`),
  ADD KEY `id_categoria` (`id_categoria`);

--
-- Indices de la tabla `resguardante`
--
ALTER TABLE `resguardante`
  ADD PRIMARY KEY (`id_resguardante`);

--
-- Indices de la tabla `responsable`
--
ALTER TABLE `responsable`
  ADD PRIMARY KEY (`id_responsable`);

--
-- Indices de la tabla `transaccion`
--
ALTER TABLE `transaccion`
  ADD PRIMARY KEY (`id_transaccion`),
  ADD KEY `id_producto_lpn` (`id_producto_lpn`);

--
-- Indices de la tabla `ubicacion`
--
ALTER TABLE `ubicacion`
  ADD PRIMARY KEY (`id_ubicacion`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id_usuario`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `categoria`
--
ALTER TABLE `categoria`
  MODIFY `id_categoria` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `estado`
--
ALTER TABLE `estado`
  MODIFY `id_estado` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `inventario`
--
ALTER TABLE `inventario`
  MODIFY `id_inventario` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `productolpn`
--
ALTER TABLE `productolpn`
  MODIFY `id_producto_lpn` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `productosku`
--
ALTER TABLE `productosku`
  MODIFY `id_producto_sku` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `resguardante`
--
ALTER TABLE `resguardante`
  MODIFY `id_resguardante` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `responsable`
--
ALTER TABLE `responsable`
  MODIFY `id_responsable` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `transaccion`
--
ALTER TABLE `transaccion`
  MODIFY `id_transaccion` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `ubicacion`
--
ALTER TABLE `ubicacion`
  MODIFY `id_ubicacion` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `inventario`
--
ALTER TABLE `inventario`
  ADD CONSTRAINT `inventario_ibfk_1` FOREIGN KEY (`id_producto_sku`) REFERENCES `productosku` (`id_producto_sku`);

--
-- Filtros para la tabla `productolpn`
--
ALTER TABLE `productolpn`
  ADD CONSTRAINT `productolpn_ibfk_1` FOREIGN KEY (`id_producto_sku`) REFERENCES `productosku` (`id_producto_sku`),
  ADD CONSTRAINT `productolpn_ibfk_2` FOREIGN KEY (`id_ubicacion`) REFERENCES `ubicacion` (`id_ubicacion`),
  ADD CONSTRAINT `productolpn_ibfk_3` FOREIGN KEY (`id_estado`) REFERENCES `estado` (`id_estado`),
  ADD CONSTRAINT `productolpn_ibfk_4` FOREIGN KEY (`id_resguardante`) REFERENCES `resguardante` (`id_resguardante`),
  ADD CONSTRAINT `productolpn_ibfk_5` FOREIGN KEY (`id_responsable`) REFERENCES `responsable` (`id_responsable`);

--
-- Filtros para la tabla `productosku`
--
ALTER TABLE `productosku`
  ADD CONSTRAINT `productosku_ibfk_1` FOREIGN KEY (`id_categoria`) REFERENCES `categoria` (`id_categoria`);

--
-- Filtros para la tabla `transaccion`
--
ALTER TABLE `transaccion`
  ADD CONSTRAINT `transaccion_ibfk_1` FOREIGN KEY (`id_producto_lpn`) REFERENCES `productolpn` (`id_producto_lpn`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
